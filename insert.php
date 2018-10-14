<?php
$username = $_REQUEST['username'];
$message = $_REQUEST['msg'];
$chat = $_REQUEST['groupCode'];

//$message = mysqli_real_escape_string($conn, $message);
//$username = mysqli_real_escape_string($conn, $username);

require_once 'loginScript.php';


$query ="INSERT INTO $chat (message, username)
VALUES ('$message', '$username')";

$myPDO->query($query);

$query2 = "SELECT * FROM $chat";

$result = $myPDO->query($query2);

$resultArray = $result->fetchAll( );

foreach($resultArray as $row)
 {
    echo '<b>'.$row['3'].'</b>: '.$row['1'].'</br>';
 }
	
 mysqli_free_result($result);

?>