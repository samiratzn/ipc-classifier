"""Provide convenient factories to generate objects used in tests"""
import factory
from classifier import models

class PatentModelFactory(factory.Factory):
    class Meta:
        model = models.PatentDocument

    title = "method of forming a treated fiber and a treated fiber formed therefrom"
    ipcs = 'D01D00106'
    list_ipc = ["D01F00110", "D01F00604", "D01F00606"]
    number = 'WO012006320010322'
    abstract = "the present disclosure is directed to a method of forming a treated fiber. a molten polymer is delivered to a fiber spinning assembly adapted to form and distribute polymer streams. at least one treatment is applied in a liquid state to at least one region on the surface of at least one molten polymer stream within the fiber spinning assembly. a substantial portion of the treatment remains on the surface of the resulting fiber within the treated region. one or more regions on the surface of the molten polymer may be treated with one or multiple treatments. the degree of coverage may vary from little coverage to complete coverage of the fiber surface. the treated regions may be in contact with one another or may be separate and distinct. a nonwoven web may be produced with selectively treated fiber regions by designing one or more fiber spinning assemblies to treat selected fibers or to apply multiple treatments. the regions of the nonwoven web may vary in treatment type, amount, or degree of coverage."
