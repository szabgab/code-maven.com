<form method="GET">
<input name="person_name">
<input type="submit" value="Echo">
</form>

<?php
    echo "Hello " . htmlspecialchars($_GET["person_name"]);
?>
