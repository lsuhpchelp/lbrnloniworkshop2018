# 1st LBRN/LONI Scientific Computing Bootcamp

Repository for 1st LBRN/LONI Scientific Computing Bootcamp

# Start Jupyter Notebook on SuperMike2

## 1. From your *local* terminal:
<pre>
$ ssh hpctrn??@mike.hpc.lsu.edu <b># replace ?? with your training account number</b>
hpctrn??@mike.hpc.lsu.edu's password: <b># type in the long password, the input will NOT echo back</b>
</pre>

## 2. Start an interactive job so that you are on a compute node either in the shelob queue or training queue:
If your training account number is less than or equal to 32 (e.g. `hpctrn01 ~ hpctrn32`):
<pre>
[hpctrn??@mike1 ~]$ qsub -I -l nodes=1:ppn=16,walltime=8:00:00 <b>-q shelob</b> -A hpc_train_2018
...
</pre>
If your training account number is larger than 32 (`hpctrn33 ~ hpctrn60`):
<pre>
[hpctrn??@mike1 ~]$ qsub -I -l nodes=1:ppn=16,walltime=8:00:00 <b>-q training</b> -A hpc_train_2018
...
</pre>

## 3. Remove the old folder `lbrnloniworkshop2018`
<pre>
[hpctrn??@mike001 ~]$ rm -rf lbrnloniworkshop2018
</pre>

## 4. Get updated Bootcamp repository:
<pre>
[hpctrn??@mike001 ~]$ git clone https://github.com/lsuhpchelp/lbrnloniworkshop2018.git
</pre>

## 5. Start Jupyter notebook from the compute node:
<pre>
[hpctrn??@mike001 ~]$ jupyter-notebook --ip $(hostname -a)
...lots of output...
The Jupyter Notebook is running at:
http://mike001.hpc.lsu.edu:8888/?token=81c778660e71ddcd49e66731fb67eed84d37319cbf51da35
</pre>

## 6. Copy and paste the above link to your browser to use Jupyter Notebook

