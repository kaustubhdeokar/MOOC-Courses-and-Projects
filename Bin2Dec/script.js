function myfun(){

	var a = document.getElementById("numinput").value;

	var pattern = /[^0-1]/g;

	var result = a.match(pattern);

	if(result==null){
		var power = a.length-1;
		var answer = 0;
		for(i=0;i<a.length;i++){
			if(a[i]==1){
			answer+= Math.pow(2,power)
			}
			power--;
		}
		alert(answer);
	}
	else{
		alert("Enter text containing only 0/1s");
	}

		document.getElementById("demo").innerHTML = answer;

}
