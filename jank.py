import sys
import time

def F(*args, **kwargs):
    if len(args) == 0:
        args = [lambda x: x]

    def fn(*aa, **kk):
        for a in args[::-1]:
            aa = [a(*aa, **kk)]
        return aa[0]
    
    class fn_obj:
        def __init__(self):
            self.par = None

        def __call__(self, *aa, **kk):
            return fn(*aa, **kk) 

        def __truediv__(self, o):
            self.par = int(o)
            return self

        def __matmul__(self, lst):
            if self.par is None:
                return list(map(self, lst)) 
            if not 'pathos.multiprocessing' in sys.modules:
                global PathosPool
                global cpu_count
                from pathos.multiprocessing import ProcessingPool as PathosPool
                from pathos.multiprocessing import cpu_count
            with PathosPool(processes=self.par if self.par > 0 else cpu_count()) as pool:
                return pool.map(fn, lst)

                
    return fn_obj()

class T:
    def __init__(self, v, *args, **kwargs):
        v, t = T.vt(v, *args, **kwargs)
        T.display(t)
        return v

    @staticmethod
    def display(t):
        if t < 1e-6:
            s = "%.2f us" % (t*1e6)
        elif t < 1e-3:
            s = "%.2f ms" % (t*1e3)
        elif t < 60:
            s  = "%.2f s" % t
        elif t < 3600:
            s = "%d min %d s" % (t//60, t-t//60) 
        else:
            s = "%d hr %d min" % (t//3600, round((t-t//3600)/60))
            
        print("Took", s)

    @staticmethod
    def t(v, *args, **kwargs):
        _, t = T.vt(v, *args, **kwargs)
        return t

    @staticmethod
    def vt(v, *args, **kwargs):
        return T.measure(time.time, v, *args, **kwargs)

    @staticmethod
    def cpu(v, *args, **kwargs):
        return T.measure(time.process_time, v, *args, **kwargs)

    @staticmethod
    def measure(timer, v, *args, **kwargs):
        t0 = timer()
        if type(v) == str:
            exec(v)
            ret = None
        else:
            ret = v(*args, **kwargs)
        return ret, timer() - t0
