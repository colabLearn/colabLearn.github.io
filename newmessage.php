
<?php
session_start();

if(  isset($_SESSION['username']) &&
     isset($_SESSION['groupname'])&&
	 isset($_SESSION['currentG'])

)

{
	$username = $_SESSION['username'];
	$groupCode =$_SESSION['groupCode'];
}

else 
{
	echo "<script type=\"text/javascript\">";
	echo "location.replace(\"groupLogin.php\")";
	echo "</script>";
}

//if (isset($_POST["end"]))
//{
	//session_start();
	//$_SESSION['username']=$username;
	//echo "<script type=\"text/javascript\">";
	//echo "location.replace(\"endSession.php\")";
	//echo "</script>";
//}

$cookie_name = 'username';
$cookie_value = $_SESSION['username'];

setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
echo <<<_END

<html>
<head>
<script src="jquery-3.3.1.min.js"></script>
<style>

h3 { background-color:LightCyan; color: Navy; text-align: center; font-size:XX-large;}
.container {
    width: 100%;
    height: 300px;
    background: lightgrey;
    margin: auto;
    padding: 10px;
}
#chatlogs {
    width: 50%;
    height: 300px;
    background: LightCyan;
    float: left;
    overflow-y : scroll;
    overflow-x : hidden;
}
#two {
    margin-left: 15%;
    height: 300px;
    background: LightCyan;
    overflow-y : scroll;
    overflow-x : hidden;
}


#three {
    
    width: 50%;
    background: lightgrey;
    
}

</style>
<title>Colab-Learn Chat box</title>

<h3> Group Session </h3>
<script type="text/javascript">
function submitChat() {
    var username = '$username';
    var groupCode= '$groupCode';
   var msg = colab.message.value;
   var xmlhttp= new XMLHttpRequest();
  xmlhttp.onreadystatechange = function ()
	{  
    		if ((xmlhttp.readyState ==4) && (xmlhttp.status==200)){
    		
    		  document.getElementById('chatlogs').innerHTML=xmlhttp.responseText;
    		
    		}
    		
    }
    xmlhttp.open('GET', 'insert.php?username='+username+'&msg='+msg+'&groupCode='+groupCode, true);
	xmlhttp.send();
	
   colab.message.value=""; 
}
    		
$(document).ready(function(e) {
    		$.ajaxSetup({cache:false});
    		setInterval(function() { $('#chatlogs').load('$groupCode.php');}, 2000);
});
</script>
   
    		
<script>
  setInterval(function() {chatlogs.scrollTop = chatlogs.scrollHeight;;}, 2000);
</script>
<body  bgcolor="LightGray" >
    		
  <form name="colab"  action="chatroom.php" method ="post">
   <section class="container">
    <div id="chatlogs"></div>
    
    		
 <div id="two">
    		In this session you will discuss your rating of each item within your group
and reach a joint consensus about rating for each item. The final rating for 
		all item shall be based on your group discussion and collective 
		reasoning/agreement of you group. <br>
    		<b>please wait for the others to finish their individual rating session and login
		to start discussion on your group rating of the items.</b> </br>
When you have completed rating the items based on your discussion and group agreement, choose a group
 		member to type your final rating of all items for example: item1=14, item2=2 ...
		in the chat room, all group member should confirm it is correct as agreed within the group. </br>
    		<b>The items</b>: <b>(Box of matches)</b>, <b>( Food concentrate)</b>, <b>(50 feet of nylon rope)</b>, <b>(Parachute silk)</b>,
    		<b>(Portable heating unit)</b>, <b>(Two .45 caliber pistols)</b>,<b>(One case of dehydrated milk)</b>,
    		<b>(Two 100 lb. tanks of oxygen)</b>,<b>(Stellar map)</b>, <b>(Self-inflating life raft)</b>, 
    		<b>(Magnetic compass)</b>, <b>(20 liters of water)</b>, <b>(Signal flares)</b>, 
    		<b>(First aid kit, including injection needle)</b>, <b>(Solar-powered FM receiver-transmitter)</b>.
    </div>
  </section>

    <div id="three"> 
<center> <textarea name="message" rows="2" cols="57" style="border:solid 3px lightcyan; placeholder="Type and send text here to chat..." "> </textarea><br>
<input type ="button" onclick="submitChat()" value="send text">
  </center>
 </div>
    		
     
<center><input type ="button" id="end" onclick="parent.end()" value="End group session">
 
    		
 </form> 
</body>
</head>
</html>
_END
?>