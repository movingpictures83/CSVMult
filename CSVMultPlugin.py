import sys
import numpy
import PyPluMA


class CSVMultPlugin:
   def input(self, filename):
      self.txtfile = open(filename, 'r')
      self.parameters = dict()
      for line in self.txtfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()
      if len(PyPluMA.prefix()) != 0:
         self.parameters['csvfile'] = PyPluMA.prefix() + "/" + self.parameters['csvfile']

   def run(self):
      filestuff = open(self.parameters['csvfile'], 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = numpy.zeros([self.m, self.n])
      i = 0
      for i in range(self.m):
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               value = float(contents[j+1])
               self.ADJ[i][j] = value
            i += 1

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write(self.firstline)
      for i in range(self.m):
         sum = float(0.0)
         for j in range(self.n):
            sum += self.ADJ[i][j]
         for j in range(self.n):
            self.ADJ[i][j] *= float(self.parameters['constant'])
            
      for i in range(self.m):
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.ADJ[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



