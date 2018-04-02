<form method="POST">
<input name="person_name">
<input type="submit" value="Echo">
</form>

<?php
    echo "Hello " . htmlspecialchars($_POST["person_name"]);
?>
