<!DOCTYPE html>
<html>
<head>
	<title>teste</title>
	<style>
	body{
		display:flex;
		align-items: center;
		justify-content: center;

	}
	</style>
</head>
<body>
<?php

$letra = $_GET['dado'];
$i = 0;
$p = 0;

$con = mysqli_connect("localhost","root","","banco");

$search = "SELECT num, id from teste where nome like '%$letra%'";
$pes = mysqli_query($con , $search);
while($alt = mysqli_fetch_array($pes)){
	$i = $i + 1;
	$id = $alt['id'];


	$codigo = "UPDATE teste SET num = '$i' WHERE id = '$id'";
	$alter = mysqli_query($con , $codigo);
	
			$p = $alt['num'];
}
if($p == null){
	echo "não existe";
}else{

$a = $_GET['num'];

if($a == 2){
	$b = 2;
	$a = 1;
}

if($a == 3){
	$b = 3;
	$a = 2;
}

if($a > 3){
	$b = $a;
	$a = $a - 1;
}
$b = $a + 1;
$c = $b + 1;
$d = $c + 1;
$e = $d + 1;
$f = $e + 1;




$ma = $_GET['num'] * 18;
$me = ($_GET['num'] * 18) - 18;
$query = "SELECT nome from teste where num > '$me' and num <= '$ma' and nome like '%$letra%'";
$sql = mysqli_query($con , $query);

while($row = mysqli_fetch_array($sql)){
	echo $row['nome'];                 
	echo"<br>";
}
if ($p > 0 && $p <=18){

}
if($p > 18 && $p <= 36){ ?>
<a href="teste.php?num=<?php echo $a;?>&dado=<?php echo $letra;?>"><?php  echo $a; ?></a>
<a href="teste.php?num=<?php echo $b;?>&dado=<?php echo $letra;?>"><?php  echo $b; ?></a>

<?php }

elseif($p > 36 && $p <= 54){
$a = 1;
$b = 2;
$c = 3;
 ?>
<a href="teste.php?num=<?php echo $a;?>&dado=<?php echo $letra;?>"><?php  echo $a; ?></a>
<a href="teste.php?num=<?php echo $b;?>&dado=<?php echo $letra;?>"><?php  echo $b; ?></a>
<a href="teste.php?num=<?php echo $c;?>&dado=<?php echo $letra;?>"><?php  echo $c; ?></a>
<?php }

elseif($p > 54 && $p <=72){ 
$a = 1;
$b = 2;
$c = 3;
$d = 4;

	?>
<a href="teste.php?num=<?php echo $a;?>&dado=<?php echo $letra;?>"><?php  echo $a; ?></a>
<a href="teste.php?num=<?php echo $b;?>&dado=<?php echo $letra;?>"><?php  echo $b; ?></a>
<a href="teste.php?num=<?php echo $c;?>&dado=<?php echo $letra;?>"><?php  echo $c; ?></a>
<a href="teste.php?num=<?php echo $d;?>&dado=<?php echo $letra;?>"><?php  echo $d; ?></a>
<?php }

elseif($p > 72 && $p <= 90){ 
$a = 1;
$b = 2;
$c = 3;
$d = 4;
$e = 5;
	?>
<a href="teste.php?num=<?php echo $a;?>&dado=<?php echo $letra;?>"><?php  echo $a; ?></a>
<a href="teste.php?num=<?php echo $b;?>&dado=<?php echo $letra;?>"><?php  echo $b; ?></a>
<a href="teste.php?num=<?php echo $c;?>&dado=<?php echo $letra;?>"><?php  echo $c; ?></a>
<a href="teste.php?num=<?php echo $d;?>&dado=<?php echo $letra;?>"><?php  echo $d; ?></a>
<a href="teste.php?num=<?php echo $e;?>&dado=<?php echo $letra;?>"><?php  echo $e; ?></a>
<?php }

 if($p > 90){ ?>
<a href="teste.php?num=<?php echo $a;?>&dado=<?php echo $letra;?>"><?php  echo $a; ?></a>
<a href="teste.php?num=<?php echo $b;?>&dado=<?php echo $letra;?>"><?php  echo $b; ?></a>
<a href="teste.php?num=<?php echo $c;?>&dado=<?php echo $letra;?>"><?php  echo $c; ?></a>
<a href="teste.php?num=<?php echo $d;?>&dado=<?php echo $letra;?>"><?php  echo $d; ?></a>
<a href="teste.php?num=<?php echo $e;?>&dado=<?php echo $letra;?>"><?php  echo $e; ?></a>
<a href="teste.php?num=<?php echo $f;?>&dado=<?php echo $letra;?>"><?php  echo $f; ?></a>

<?php } 
}
?>
</body>
</html>