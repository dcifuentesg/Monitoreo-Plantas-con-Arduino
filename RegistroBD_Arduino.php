$CN=mysqli_connect('localhost', 'id18775540_noob1', 'VFwQL{*oB7x|iTVT', 'id18775540_esp8266');
    
$temperature = $_GET["temperature"];
$humidityA = $_GET["humidityA"]; 
$humidityS = $_GET["humidityS"]; 
$light = $_GET["light"]; 

$IQ="insert into `LecturasArduino`(temperature,humidityA,humidityS,light) values('$temperatura','$humidity','$humedadaire','$ligth')";
