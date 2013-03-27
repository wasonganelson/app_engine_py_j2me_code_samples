<?php
$page = file_get_contents("1.txt");
$page = strip_tags($page);
echo $page;
?>
