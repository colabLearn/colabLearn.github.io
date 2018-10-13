<?php

require_once 'loginScript.php';

if (isset ($_POST['userCode'])) 
		
      {
	 if (isset ($_POST['iCode']))

	
	{

	    $iCode = $_POST['iCode'];
	
	    $query = "SELECT groupname FROM p_groups WHERE invite = '$iCode';";
      
         $result = $myPDO->query($query);
	    
	    if($result)
		{
		   $query2 = "SELECT COUNT (groupname) FROM p_groups WHERE invite = '$iCode';";
		   
            $count = $myPDO->query($query2);
               	   
		   $resultArray = $count->fetchAll( );
		   
		   $count = $resultArray[0][0];
		   
		   if ($count>0)
		   {
		   	 $resultArray2 = $result->fetchAll();
		   	 $groupCode = $resultArray2[0][0];
		   	 
		   	 echo $groupCode;
		   	 session_start();
		   	 $_SESSION['userCode']=$iCode;
		   	 $_SESSION['groupCode']=$groupCode;
		   	 
		   	 echo "<script type=\"text/javascript\">";
		   	 echo "location.replace(\"participantDataPage.php\")";
		   	 echo "</script>";
		   }
		   else 
		   {
		   	
		   	 //header('Refresh:5; url=participantLogin.php');
			 echo "<script type=\"text/javascript\">";
		   	 echo "alert('Please enter correct invite code')";
		   	 echo "</script>";
		   	 //echo '<b><font color=\"red\">Please enter correct invite code</font></b>';
		   }
		   
	    
         }
	}


      }
echo <<<_END

<style>
h4 { background-color:LightCyan; color: Navy; text-align: center; font-size:X-large;}
	
		
		
</style>
<h4> Please login with your invite code, thank you.</h4>
<body bgcolor="LightGray">

<div style="width: 60%; margin: 0px auto;">
<table border="0" cellpadding ="2" cellspacing="5" bgcolor="#eeeeee">
<th colspan="2" align ="center">Login Form</th>

<form method ="post" action="participantLogin.php" autocomplete='off'>
<tr><td>Please enter your invite code here:</td>
<td><input type="text" maxlength="10" name="iCode" placeholder='Invite Code' required='required'></td></tr>
<tr><td colspan="2" align="center">
<input type="submit" name ="userCode" value="Login"></td></tr>

</form>
</table>
</div>
</body>
_END;

?>