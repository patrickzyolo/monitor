<?php
    if (!mysql_connect('odroid-u3.local', 'monitor', 'test123'))
	{
		echo "Konnte nicht zu mysql verbinden: " . mysql_error() . "\n";
		exit;
	}

	mysql_select_db('monitor');
	mysql_set_charset('utf8');
	mysql_query("SET NAMES 'utf8'");
	date_default_timezone_set('UTC');

	$today = date("Ymd");
	$data = mysql_query("select * from data{$today}");
    $news = mysql_query("select * from news{$today}");
    $headlines = array();
	$clusters = array();

    $end = array();

	while ($dataset = mysql_fetch_row($data))
	{
		$clusters[$dataset[0]] = (int) $dataset[1];
	}

    while ($lines = mysql_fetch_row($news))
	{
		array_push($headlines, $lines[0]);
	}

	arsort($clusters);

    // echo json_encode($clusters);

    foreach ($clusters as $name => $name_count)
    {
        $tmp_1 = array();
        $tmp_1["name"] = $name;
        $tmp_1["size"] = $name_count;
        $tmp_1["imports"] = array();

        foreach ($headlines as $line)
        {
            if (strpos($line, $name) !== false)
            {
                foreach ($clusters as $name_2 => $name_cluster_2)
                {
                    if (strpos($line, $name_2) !== false)
                    {
                        if ($tmp_1["imports"])
                        {
                            if (!in_array($name_2, $tmp_1["imports"]) && $name != $name_2)
                            {
                                array_push($tmp_1["imports"], $name_2);
                            }
                        }
                        else
                        {
                            if ($name != $name_2)
                            {
                                $tmp_1["imports"] = array($name_2);
                            }
                        }
                        // echo "<p>" . $name . "</p>\n";
                    }
                }
            }
        }
        array_push($end, $tmp_1);
    }

    echo json_encode($end);
?>
