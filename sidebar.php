<html>
    <head>
    <meta http-equiv="refresh" content="2">
    </head>
    <body>
  

<?php 
session_start();

if(  isset($_SESSION['username']) &&
		isset($_SESSION['groupCode'])&&
	 isset($_SESSION['currentG'])

)
{
	$currentuser = $_SESSION['currentG'];
}
require_once 'loginScript.php';

$query ="Select *From $currentuser;";

$result = $myPDO->query($query);


if($result)
{ 
	echo '<b>'.'Current user(s):'.'</b>'.'</br>';
	$resultArray = $result->fetchAll( );
	
	$nameArray = array_column($resultArray, 'username');
	
	foreach ($nameArray as $name)
		{
		  echo $name.'</br>';
		}
	
	//while($row=mysqli_fetch_row($result))
	//{
	 //  echo $row['1'].'</br>';
	//}
	//mysqli_free_result($result);
}



mysqli_close($conn);


?>

    
 


    </body>
</html>

