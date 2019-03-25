if(navigator.geolocation)
{
		navigator.geolocation.getCurrentPosition(onPositionReceived);
}

function onPositionReceived(position)
{
	var data = new Array();
	data['user_lat'] = position.coords.latitude;
	data['user_lon'] = position.coords.longitude;

	document.getElementById("id_latitude").value = position.coords.latitude;
	document.getElementById('id_longitude').value = position.coords.longitude;

}