<?php    
    $CN=mysqli_connect('localhost', 'id18775540_noob1', 'VFwQL{*oB7x|iTVT', 'id18775540_esp8266');
    $IQ="SELECT * FROM `LecturasArduino2`";
    $R=mysqli_query($CN,$IQ);
    $numeros = mysqli_fetch_all($R, MYSQLI_ASSOC);
    $Message="";
    foreach($numeros as $numero){
			$Message=$Message.$numero['temperature'].",".$numero['humidityA'].",".$numero['humidityS'].",".$numero['light'].";";
	}
	echo $Message;
?>