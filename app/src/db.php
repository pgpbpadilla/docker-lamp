<?php
$conn = new mysqli(
    "db",
    "root",
    "example",
    "app"
);

if ($conn->connect_errno) {
    echo "Failed to connect to MySQL: (" . $conn->connect_errno . ") " . $conn->connect_error;
}

echo "Connected to:" . $conn->host_info . "<br>";

$query = "SELECT * FROM user";

if ($result = $conn->query($query)) {
    /* fetch associative array */
    echo "Listing all users:";
    echo "<div>";
        while ($row = $result->fetch_assoc()) {
            echo $row["name"] . "<br>";
        }
    echo "</div>";
    /* free result set */
    $result->free();
}
$conn->close();
?>
