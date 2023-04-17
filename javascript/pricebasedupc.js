/*

UPC Check Digit Library

* Calculating the check digit for 4-digit prices
* Calculating the check digit for UPCs (GTIN-12)

*/


function padleft( s, padstring, totallength ) {
	var addedlength = totallength - s.length;
	return repeatstring( padstring, addedlength )+s;
}

// repeats a string count times
function repeatstring( s, count ){
	var out = "";
	for (var i = 0; i < count; i++) {
		out += s;	
	}
	return out;
}

function iseven( n ) {
	return (n % 2 == 0);
}

function isodd( n ){
	return !iseven(n);
}

function digitposition( number, position ) {
	// returns the digit in position of number
	return number.toFixed()[position];
}

// ================================================================

function weightfactor2minus( digit ) {
	// "The digit is multiplied by 2. If the result has two digits, the tens digit is subtracted from the units digit. The units digit resulting is the weighted product."
	// 0 <= digit <= 9
	var return_value = [0,2,4,6,8,9,1,3,5,7];
	return return_value[digit];
}
function weightfactor3( digit ) {
	// "The digit is multiplied by 3. The unit's digit of the result is the weighted product."
	// 0 <= digit <= 9
	var return_value = [0,3,6,9,2,5,8,1,4,7];
	return return_value[digit];		
}
function weightfactor5plus( digit ) {
	// "The digit is multiplied by 5. The units digit and the tens digit of the result are added together. the result of this sum is the weighted product."
	// 0 <= digit <= 9
	var return_value = [0,5,1,6,2,7,3,8,4,9];
	return return_value[digit];
}
function weightfactor5minus( digit ) {
	// "The digit is multiplied by 5. The tens digit of the result is subtracted from the result. The unit's digit of the result of this subtraction is weighted product."
	// 0 <= digit <= 9
	var return_value = [0,5,9,4,8,3,7,2,6,1];
	return return_value[digit];
}

// ================================================================

function getweightfunction( position ) {
	// returns function to cal
	// position is 0-indexed
	
	if (typeof(position) != 'number') {
		throw "getweightfunction: incorrect type";		
	}
	
	var out = null;
	
	switch (position) {
	case 0:
		out = weightfactor2minus;
		break;
	case 1:
		out = weightfactor2minus;
		break;
	case 2:
		out = weightfactor3;
		break;
	case 3:
		out = weightfactor5minus;
		break;
	default:
		break;
		
		
	}

	return out;

}

// ================================================================

function formatfourdigitprice( price ) {
	// price is float
	// convert to decimal-less
	// 0 <= price <= 9999
	
	var MIN_PRICE = 0;
	var MAX_PRICE = 99.99;
	
	if (
		(price < MIN_PRICE)||
		(price > MAX_PRICE)
	) {
		
		throw "formatfourdigitprice: Out of bounds";
	}
	
	price *= 100;
	
	var formattedpricestring = padleft( price.toFixed(), "0", 4);
	
	return formattedpricestring;
}


function fourdigitpricechecksum( formattedpricestring ) {
	// #### 1. Determine the weighted product for each number in Positions One to Four according to the assigne weighting factors.
	var out = null;


	// split price string into array
	var pricearray = formattedpricestring.split('')
	//out = pricearray;
	
	// convert array elements to weighted value 
	var weightedpricearray = []
	for (var i = 0; i < pricearray.length;i++) {
		
		var weightedfunction = getweightfunction(i);
		weightedpricearray[i] = (getweightfunction(i))(pricearray[i]);
		
		
	}
	
	
	// #### 2. Add the products of step 1.
	var weightedpricearray_sum = 
		weightedpricearray.reduce(
			(accumulator, currentValue) => accumulator + currentValue,
			0
		);

	// #### 3. Multiply the result of step 2 by the factor 3. The unit's digit of the result is the check digit.
	weightedpricearray_sum *= 3;
	var weightedpricearray_sum_unit = digitposition(weightedpricearray_sum,1);
	
	out = weightedpricearray_sum_unit;
	return out;
}



function calculateUPCchecksum( upc_nochecksum ) {
	// returns single digit checksum	
	// upc_nochecksum is string, length == 11
	
	if ( typeof(upc_nochecksum) != "string" ) {
		throw "calculateUPCchecksum: upc_nochecksum: incorrect type: "+typeof(upc_nochecksum);		
	}
	if ( upc_nochecksum.length != 11 ) {
		throw "calculateUPCchecksum: upc_nochecksum: incorrect length: "+upc_nochecksum.length;	
	}
	
	
	// 1: multiply each digit by 1 (if even index) or 3 (if odd index)
	
	var upc_nochecksum_array = upc_nochecksum.split('');
	// must reverse array
	upc_nochecksum_array.reverse();
	
	var upc_nochecksum_array_int = upc_nochecksum_array.map( (x) => parseInt(x) );
	
	var upc_nochecksum_array_int_adjusted = new Array(upc_nochecksum_array_int.length);
	
	for (var i = 0; i < upc_nochecksum_array_int.length; i++) {
		// multiple each digit from right to left

		
		
		if (isodd(i+1)) {
			// if odd, multiply by 3
			// i is 0-indexed

			upc_nochecksum_array_int_adjusted[i] = upc_nochecksum_array_int[i] * 3;
		
		} else {
			// if even, multiply by 1
			upc_nochecksum_array_int_adjusted[i] = upc_nochecksum_array_int[i];
		}
		
	} 

	// 2: sum the elements of the array
	
	var upc_array_sum = upc_nochecksum_array_int_adjusted.reduce(
		(accumulator, currentValue) => accumulator + currentValue,
		0
	);
	
	// 3: Subtract sum from nearest equal or higher multiple of ten
	
	upc_array_sum %= 10;
	if (upc_array_sum != 0) {
		upc_array_sum = 10 - upc_array_sum;
	}
	
	return upc_array_sum;
}

// TODO: convert UPC to class
class UPC {
	#strData = ""
	#arrData = []
	
	constructor() {}

}


