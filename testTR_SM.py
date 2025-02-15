import pyimagesearch.TRIndexer as TR
import pyimagesearch.TRSolver as TRS
import os
import pyimagesearch.SFIndexer as SF
import pyimagesearch.SFSolver as SFS
import pyimagesearch.TFSFIndexer as TFSF
import pyimagesearch.TFSFSolver as TFSFS
import pyimagesearch.TRgraphplot as TRP

import cProfile
import time

#TR.TagIndex()
TR_Result = TRS.TRSolver("queryimage.jpg")
#cProfile.run("TRS.TRSolver('test'+os.sep+'data'+os.sep+'train'+os.sep+'0253_421644823.jpg')")
print TR_Result.result
#idf = TR_Result.tf.idf_
#print dict(zip(TR_Result.tf.get_feature_names(), idf))
#TRP.PlotTR(TR_Result.tfidf_matrix)

#all = image_classify then consolidate
#SF.SemanticFeatureIndex("consolidate")
#SF.SemanticFeatureIndex("all")
#x = SFS.SemanticFeatureSolver(".." + os.sep+".." + os.sep + "queryimage.jpg")
#cProfile.run('SFS.SemanticFeatureSolver(".." + os.sep+".." + os.sep + "queryimage.jpg")')
#print x.result

# TFSF.SemanticFeatureIndex()
# cProfile.run("TFSFS.SemanticFeatureSolver('queryimage.jpg')")
# x = TFSFS.SemanticFeatureSolver("queryimage.jpg")
# print x.result[0:16]
