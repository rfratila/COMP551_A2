import pylab  # for graphing
import pickle
import sys

modelName = "stats.pickle"
if len(sys.argv) > 1:
    modelName = sys.argv[1]
with open('%s' % modelName) as infile:
    if '.pickle' in modelName:
        data = pickle.load(infile)

pylab.plot(data['epoch'], data['error'], '-ro', label='Test Error')
pylab.plot(data['epoch'], data['accuracy'], '-go', label='Test Accuracy')
pylab.xlabel("Epoch")
pylab.ylabel("Error (%)")
pylab.ylim(0, max(data['error']) if max(data['error']) < 20000 else 20000)
pylab.title(modelName)
pylab.legend(loc='upper right')
# pylab.savefig('.png'%modelName)
pylab.show()  # enter param False if running in iterative mode
