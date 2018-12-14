<?php
$nome = $_POST['nome'];
$senha = $_POST['senha'];
$email = $_POST['email'];

$con = mysqli_connect("localhost","root","","banco");
$insert = "INSERT into user(nome , senha, email, logado) VALUES ('$nome','$senha','$email', 1)";
$query = mysqli_query($con, $insert);
header('Location:../home.html');