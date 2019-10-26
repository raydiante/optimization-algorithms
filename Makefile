all:
	python tabu.py < g200-4-05.dat > resultados.txt
	python tabu.py < g75-4-01.dat > resultados.txt
	python tabu.py < le450_15a.g > resultados.txt
	python tabu.py < g100-4-02.dat > resultados.txt
	python tabu.py < g25-4-05.dat > resultados.txt
	python tabu.py < g200-4-01.dat > resultados.txt

	python metaheuristica.py < g200-4-05.dat > resultados.txt
	python metaheuristica.py < g75-4-01.dat > resultados.txt
	python metaheuristica.py < le450_15a.g > resultados.txt
	python metaheuristica.py < g100-4-02.dat > resultados.txt
	python metaheuristica.py < g25-4-05.dat > resultados.txt
	python metaheuristica.py < g200-4-01.dat > resultados.txt

	python genetico2.py < g200-4-05.dat > resultados.txt
	python genetico2.py < g75-4-01.dat > resultados.txt
	python genetico2.py < le450_15a.g > resultados.txt
	python genetico2.py < g100-4-02.dat > resultados.txt
	python genetico2.py < g25-4-05.dat > resultados.txt
	python genetico2.py < g200-4-01.dat > resultados.txt

	python simulatedannealing.py < g200-4-05.dat > resultados.txt
	python simulatedannealing.py < g75-4-01.dat > resultados.txt
	python simulatedannealing.py < le450_15a.g > resultados.txt
	python simulatedannealing.py < g100-4-02.dat > resultados.txt
	python simulatedannealing.py < g25-4-05.dat > resultados.txt
	python simulatedannealing.py < g200-4-01.dat > resultados.txt

	python grasp.py < g200-4-05.dat > resultados.txt
	python grasp.py < g75-4-01.dat > resultados.txt
	python grasp.py < le450_15a.g > resultados.txt
	python grasp.py < g100-4-02.dat > resultados.txt
	python grasp.py < g25-4-05.dat > resultados.txt
	python grasp.py < g200-4-01.dat > resultados.txt

	python vns-kcaed3.py < g200-4-05.dat > resultados.txt
	python vns-kcaed3.py < g75-4-01.dat > resultados.txt
	python vns-kcaed3.py < le450_15a.g > resultados.txt
	python vns-kcaed3.py < g100-4-02.dat > resultados.txt
	python vns-kcaed3.py < g25-4-05.dat > resultados.txt
	python vns-kcaed3.py < g200-4-01.dat > resultados.txt