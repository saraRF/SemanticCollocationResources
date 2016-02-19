#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import gensim


def get_pmi(base, base_pos, col, col_pos):
	base_url = "http://10.80.27.67/webservice/db4/get_pmi"
	params = "?base=%s&base_pos=%s&collocative=%s&collocative_pos=%s"
	
	url = base_url + params % (base, base_pos, col, col_pos)
	response = urllib2.urlopen(url)
	content = response.read()
	
	data = json.loads(content)
	if data:
		pmi = data[6]
	else:
		pmi = 0
		
	return pmi
	
	
def get_col_candidates(model, examples, base):
	
	example = examples[0]
	result = model.most_similar(positive=[example["col"], base], negative= [example["base"]])
	
	candidates = [row[0] for row in result]
	return candidates


if __name__ == '__main__':
	
	model_path = model_path
	
	f = open(output_path, 'w')
	
	data = [
			{
			"examples": [{"base": "idea", "col": "gran"}],
			"bases": ["representación", "problema", "sorpresa", "interés", "risa", "pobreza", "frustración", "lluvia", "viento", "daño", "cambio", "crecimiento", "ruido", "paciencia", "explosión", "grado", "nivel", "frío", "creatividad", "valor"],
			"base_pos": "n",
			"col_pos": "a"
			},
			{
			"examples": [{"base": "entorno", "col": "crear"}],
			"bases": ["escándalo", "edicto", "ley", "beneficio", "crisis", "elección", "informe", "unión", "gobierno", "sistema", "medida", "orden", "radiación", "controversia", "estabilidad", "epidemia", "olor", "acuerdo", "señal", "cambio"],
			"base_pos": "n",
			"col_pos": "v"
			},
			{
			"examples": [{"base": "precio", "col": "aumentar"}],
			"bases": ["período", "estabilidad", "nivel", "sueldo", "calidad", "cobertura", "protección", "liderazgo", "capital", "competencia", "cooperación", "economía", "inteligencia", "tolerancia", "capacidad", "tasa", "gasto", "riqueza", "salud", "umbral"],
			"base_pos": "n",
			"col_pos": "v"
			},
		]
		
	model = gensim.models.Word2Vec.load(model_path)
	
	for lf_data in data:
		examples = lf_data["examples"]
		base_pos = lf_data["base_pos"]
		col_pos = lf_data["col_pos"]
		
		for base in lf_data["bases"]:
			candidates = get_col_candidates(model, examples, base)
		
			for candidate in candidates:
				pmi = get_pmi(base, base_pos, candidate, col_pos)
				#print base, candidate, pmi
				if pmi > 0.0:
					f.write("+" + base + " " + candidate + "\t" + "\n")
				else:
					f.write(base + " " + candidate + "\t" + "\n")
	
	
