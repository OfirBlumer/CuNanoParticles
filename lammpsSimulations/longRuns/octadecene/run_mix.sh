LMP=/hirshblab-storage/ofirblumer/mylammps/src/lmp_g++_openmpi

RUNDIR=/hirshblab-storage/ofirblumer/Projects/CuNanoParticles/lammpsSimulations/biased/octadeceneSolution

NCORE=48

INP='start.lmp'

#load modules and compile

module purge



# gnu compilers, this part should be the same as in install_lammps.sh that

# was used for compilation
module load gcc/gcc-8.2.0
module load python/python-anaconda_3.7
module load mpi/openmpi-4.0.5-IB


#send job

cd $RUNDIR

mpirun -np $NCORE $LMP -in $INP -screen none
