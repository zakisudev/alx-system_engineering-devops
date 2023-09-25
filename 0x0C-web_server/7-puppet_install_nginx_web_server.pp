# Add nginx stable repo
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin,
}

# Update and Upgrade software package list
exec { 'update and upgrade packages':
  command => 'apt-get update && apt-get upgrade',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Install nginx
package { 'nginx':
  ensure     => 'installed',
}

# Allow HTTP Requests to nginx
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'".
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin,
  onlyif  => '! dpkg -l nginx | egrep \ 'îi.*nginx' > /dev/null 2>&1,
}

# Update directory permissions
exec { 'chmod 222 folder':
  command => 'chmod -R 755 /var/www.
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Create index file
file { '/var/www/html/pagenotfound.html':
  content => 'Ceci n'est pas une page',
}

# Add 301 redirection and 404 error page
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content => 
  "server {
       listen 	 80 default_server;
       listen    [::]:80 default_server;
       root      /var/www/html;
       location /redirect_me {
         return 301 https://zakisu.vercel.app;
       }
       error_page 404 /pagenotfound.html;
       location /pagenotefound {
         root /var/www/html;
         internal;
       }
  }
  ",
}

# Restart nginx server after configuration
exec { 'restart service':
  command => 'systemctl nginx restart'
  path    => '/usr/bin:/usr/sbin:/bin',
}

# Start nginx service
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
