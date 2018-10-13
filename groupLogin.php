<?php
session_start();
if(isset($_SESSION['userCode']) && isset($_SESSION['groupCode']))
{
	echo "<center>"."<b>";
	echo "Chart room for participant: " . $_SESSION['groupCode'];
	echo "</b>"."</center>";
	
	$groupname = $_SESSION['groupCode'];
	$currentusers = $groupname."_users";


}

if (isset($_POST['Enter']))
{

	$username=$_POST['username'];
	if (trim($username)=='')
	{
		header('Refresh:0; url=groupLogin.php');
		echo "<script type=\"text/javascript\">";
		echo "alert('Please enter a username')";
		echo "</script>";
		exit;
	}
	else 
	{
		require_once 'loginScript.php';
		$query ="SELECT COUNT(username)FROM $currentusers WHERE username='$username';";
		$count = $myPDO->query($query);
		
		$resultArray = $count->fetchAll( );
			
		$count = $resultArray[0][0];
		if ($count>0)
		{
			header('Refresh:0; url=groupLogin.php');
			echo "<script type=\"text/javascript\">";
			echo "alert('Unsername in use, please choose another username')";
			echo "</script>";
			exit;
		}
		else 
		{
			$query2 ="INSERT INTO $currentusers (username)VALUES ('$username');";
			$myPDO->query($query2);
			session_start();
			$_SESSION['username']=$username;
			$_SESSION['groupname']=$groupname;
			$_SESSION['currentG']=$currentusers;
			echo "<script type=\"text/javascript\">";
			echo "location.replace(\"chatroom.php\")";
			echo "</script>";
		}
		
		
	}
}
else 
	
{ }

echo <<<_END
<html>
  <head>
<style>
h3 { background-color:LightCyan; color: Navy; text-align: center; font-size:XX-large;}

h4 { background-color:LightCyan; color: Navy; text-align: center; font-size:X-large;}
div { background-color:LightCyan;
	  position:relative;
	  left: 10%;
	  color: Navy;
	  text-align: justify;
	  font-size:X-large;
      border: 2px solid;
      padding: 20px;
      width: 800px;
      resize: vertical;
      overflow: auto;
}
iframe   {
		  position:relative;
	      left: 20%;
		}
span {background-color:LightCyan; color: Navy; font-size:X-large;}
a {color: black;}
</style>


    <title>Chat room</title>

   <body bgcolor="LightGray" align="center" valign="middle">

<div style="width: 60%; margin: 0px auto;">
<table border="0" cellpadding ="2" cellspacing="5" bgcolor="#eeeeee">
<th colspan="2" align ="center">Login to chat</th>
		
  <form action="groupLogin.php" method="POST">
		
 <tr><td> Please enter username of your choice:</td>
  <td><input type="text" name="username"> </td></tr>
<tr><td colspan="2" align="center">
  <input type ="submit" name="Enter"></td></tr>
 </form>
</table>
  </body>
</html>
_END;


?>
  
 
