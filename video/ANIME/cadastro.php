<!DOCTYPE html>
<html>
<head>
	<title></title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css/drop-menu.css">
	<link rel="stylesheet" type="text/css" href="css/cadastro.css">
	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
	<div id="bar"><p>qwdwqh sxqwuxyg qwsqwuhxs qxhqwuxhqusiuxqn></p> <button id="close">X</button></div>
	<div id="menu">
		<ul>
			<li><a href="#"><i class="fa fa-bars" style="font-size:24px"  id="butbar"></i></a></li>
			<li><a href="home.html">HOME</a></li>
			<li><a href="#">Animes</a></li>
			<li><a href="#" onmouseover="onove(this)" onmouseout="onout(this)" id="dop">alguma</a>
				<ul>
					<li><a href="#" onmouseover="ove(this)" onmouseout="out(this)">algo</a></li>
					<li><a href="#" onmouseover="ove(this)" onmouseout="out(this)">algo</a></li>
					<li><a href="#" onmouseover="ove(this)" onmouseout="out(this)">Outros</a></li>
				</ul>

			</li>
		</ul>
	</div>

	<center><div class="register-t">Cadastro</div>
	<div class="register-c">
		<form method="post" action="sistema/ru.php">
			<p>Use Name</p>
			<input type="text" name="nome">
			<p>Password</p>
			<input type="password">
			<p>Confirn Password</p>
			<input type="password" name="senha">
			<p>E-mail</p>
			<input type="email" name="email">
	</div>
	<div class="register-e">
	<input type="submit" value="Cadastrar" class="cds">
	</form></div></center>

<script>
// menu dropdown
var a = document.getElementById('dop'); 
function ove(obj){
	a.style.color = "rgb(61,148,188)";
	a.style.background = "rgb(20,20,20)";
}
function out(obj){
	a.style.color = "rgb(230,230,230)";
	a.style.background = "rgb(26,26,26)";
}
function onove(obj){
	a.style.color = "rgb(61,148,188)";
}
function onout(obj){
	a.style.color = "rgb(230,230,230)";
	a.style.margin = "0";
}
// fim menu dropdown

//menu bar

var menu = document.getElementById('bar');
var butbar = document.getElementById('butbar');
var close = document.getElementById('close');

butbar.onclick = function(){
	menu.style.visibility = "visible";
	menu.style.left = "0";
	menu.style.opacity = "1";
	int.style.position = "fixed";
	int.style.display = "block";
}
close.onclick = function(){
		menu.style.visibility = "hidden";
		menu.style.left = "-200px";
		menu.style.opacity = "0";
		int.style.position = "relative";
		int.style.display = "none";	
}

//fim menu bar
</script>


</body>
</html>