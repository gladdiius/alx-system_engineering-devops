# Define a class for installing Nginx and configuring it
class { 'nginx':
  ensure => 'installed',
}

# Define a class for managing the Flask application
class { 'flask_app':
  gunicorn_bind_address => '0.0.0.0:5000',
  gunicorn_workers     => 4,  # Adjust the number of Gunicorn workers as needed
  gunicorn_threads     => 25, # Adjust the number of Gunicorn threads as needed
}

# Define the Nginx vhost for the Flask application
nginx::resource::vhost { 'flask_app':
  listen_port => 80,
  server_name => 'your_server_ip',
  location    => [
    {
      'location'  => '/airbnb-onepage/',
      'proxy'     => 'http://127.0.0.1:5000',
      'set_header' => ['Host $host', 'X-Real-IP $remote_addr', 'X-Forwarded-For $proxy_add_x_forwarded_for', 'X-Forwarded-Proto $scheme'],
    },
    # Add additional location blocks if needed
  ],
  worker_processes => auto, # Use auto to set the number of worker processes automatically
  worker_connections => 1000, # Adjust the number of worker connections as needed
}

# Define a class for managing the Flask application server
class { 'flask_app::gunicorn':
  app_dir => '/path/to/your/app',
  workers => 4,  # Match the number of Gunicorn workers with the configuration in the flask_app class
  threads => 25, # Match the number of Gunicorn threads with the configuration in the flask_app class
}
