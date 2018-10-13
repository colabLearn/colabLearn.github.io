<?php
session_start();

if(  isset($_SESSION['username']) && 
     isset($_SESSION['groupCode'])&&
	 isset($_SESSION['currentG'])
		
  )
{  
	$username = $_SESSION['username'];
	$currentG = $_SESSION['currentG'];
	$_COOKIE['username'] = $_SESSION['username'];;
	
	//On page 2
	
	
}
if (isset($_POST["myButton"]))
 {
   
   $_SESSION['username']=$_COOKIE['username'];
   $_SESSION['currentG']= $currentG;
   echo "<script type=\"text/javascript\">";
   echo "location.replace(\"endSession2.php\")";
   echo "</script>";
	
 }

?>



<html>

<head>
<title>Chat room</title>
<script>
 function end() {
	    var username = '$username';
	      
	    //location.replace("endSession2.php?username=" +username);
	    location.replace("thanks.php?username=" +username);
	             
		
	  }
</script>

</head>

<FRAMESET cols="10%, 80%">
  <FRAMESET rows="*,200">
      <FRAME id='f1' src="sidebar.php">
     
  </FRAMESET>
  <FRAME id='f2' src="newmessage.php">
  
</FRAMESET>


 
	

</html>



