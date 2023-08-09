# Automated Puppet fix to find out why Apache is returning a 500 error
exec { 'fix_wordpress_500_error':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  path     => ['/bin', '/usr/bin'],  # Specify all necessary paths
  provider => shell,
  onlyif   => 'grep -q ".phpp" /var/www/html/wp-settings.php',
}
