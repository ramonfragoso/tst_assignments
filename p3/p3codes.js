////////// busca e filtra ////////////////////
var fetch = require("node_fetch");

function() filtradora(url, data, resolve) {
	var recurso = data.recurso;
	var maximo = data.maximo;
	var minimo = data.minimo

	fetch(url + "/" + recurso).then(function(response) {
		response.json().then(function(lista) {
			resolve(list.filter(e => e >= minimo && e <= maximo));
		})
	});
}

function busca_e_filtra(url_base) {
	return new Promise(function(resolve, reject) {
		fetch(url_base + "/data").then(function(response) {
			if(response.ok) {
				response.json().then(function(data) {
					filtradora(url_base, data, resolve);
				});
			}
		}, function() {
			reject();
		});
	});
}

///////////// media distancias /////////////

function aux(ponto) {
	
	return Math.sqrt(Math.pow(ponto[0], 2) + Math.pow(ponto[1], 2));
}

function media_distancias(pontos, d) {
	
	f = pontos.filter(e => e[0] > 0 && => e[1]).map(z => aux(z)).filter(g => g <= d);

	return f.reduce((a, e) => a+e, 0) / f.length;
}

///////////////////////////////////////////////////////////////
