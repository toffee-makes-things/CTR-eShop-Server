<?php
// IAS IdentityAuthenticationSOAP.php Made by Lambda 
// Made in PHP 8.1
// This will handle all SOAP Methods that Nintendo's IAS server does.

// require config. it expects this to be in /var/eshop/config edit to your liking 
include('/var/eshop/config/config.php'); 

// connect to postgres using config data. it took me a while to figure out how to correctly put variables in strings

$dbconn = pg_connect("host=${sqlhost} port=5432 dbname=${sqldatabase} user=${sqlusername} password=${sqlpassword}")


?>