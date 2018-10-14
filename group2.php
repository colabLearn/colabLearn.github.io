<?php

require_once 'loginScript.php';

$query2 = "SELECT * FROM group2 ";

$result = $myPDO->query($query2);

 $resultArray = $result->fetchAll( );
 
 foreach ($resultArray as $row)
 {
 	echo '<b>'.$row['3'].'</b>: '.$row['1'].'</br>';
 }
	
		
	
	mysqli_free_result($result);

?>