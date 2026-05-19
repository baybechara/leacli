<?php
$text.= "Имя: ".$_POST["name"];
$text.= "%0AТелефон: %2b".$_POST["full_phone"];
$text.= "%0AЦель обращения: ".$_POST["request"];
$text.= "%0A se:".$_POST["utm_source"];
$text.= "%0A mm:".$_POST["utm_medium"];
$text.= "%0A cn:".$_POST["utm_campaign"];
$text.= "%0A tm:".$_POST["utm_term"];
	
// send email
$request = file_get_contents("https://api.telegram.org/bot7188575087:AAG-2vxHRa9bO3hY1OtPQt7PmOk2HIxmToU/sendMessage?chat_id=-1002133471097&parse_mode=html&text=".$text);

$key = '1FAIpQLSeeCST1GHROgD9yemVyqnW4-CGjr2B7EL0wKlfNEgTjC5OptQ'; // <- Меняем на свой

$post_data = array (
	"entry.472950910" => $_POST['name'],
	"entry.1596992661" => $_POST['full_phone'],
	"entry.1390146765" => $_POST['request'],
	"entry.692397013" => $_POST['utm_source'],
	"entry.1479680090" => $_POST['utm_medium'],
	"entry.1001720316" => $_POST['utm_campaign'],
	"entry.238278228" => $_POST['utm_term']
);

// Далее не трогать
$url = "https://docs.google.com/forms/d/e/".$key."/formResponse";

// с помощью CURL заносим данные в таблицу google
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
$output = curl_exec($ch);
curl_close($ch);
header("Location: /thank-you.html");
?>