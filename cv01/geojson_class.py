import json

class Object(object):
    def __init__(self,type):
        self.type = type

    def to_json(self):
        return {"type": self.type}

class Geometry(Object):
    @classmethod
    def from_json(cls,adict):
        if adict["type"]=="LineString":
            obj = LineString.from_json(adict)
        elif adict["type"] == "Point":
            obj = Point.from_json(adict)
        elif adict["type"] == "Polygon":
            obj = Polygon.from_json(adict)
        return obj


    def __init__(self,type,coordinates):
        super().__init__(type)
        self.coordinates = coordinates

    def to_json(self):
        dict = super().to_json()
        dict["coordinates"] = self.coordinates
        return dict

class Feature(Object):
    @classmethod
    def from_json(cls,adict):
        properties = adict["properties"]
        geometry = Geometry.from_json(adict["geometry"])
        obj = cls(geometry,properties)
        return obj

    def __init__(self, geometry, properties, id=None):
        super().__init__("Feature")
        if not isinstance(geometry,Geometry):
            raise ValueError("Attempted to insert non Geometry as a geometry")
        self.geometry = geometry
        if id:
            self.id = id
        self.properties = properties

    def to_json(self):
        dict = super().to_json()
        dict["geometry"] = self.geometry.to_json()
        dict["properties"] = self.properties
        return dict


class FeatureCollection(Object):
    @classmethod
    def from_json(cls,adict):
        feature_objs = []
        for fdict in adict["features"]:
            fobj = Feature.from_json(fdict)
            feature_objs.append(fobj)
        obj = cls(feature_objs) # Ekvivalentni FeatureCollection(feature_objs)
        return obj

    def __init__(self,features):
        super().__init__("FeatureCollection")
        self.features = features

    def to_json(self):
        dict = super().to_json()
        features = [f.to_json() for f in self.features]
        dict["features"] = features
        return dict

class Point(Geometry):
    @classmethod
    def from_json(cls,adict):
        x = adict["coordinates"][0]
        y = adict["coordinates"][1]
        return cls(x,y)

    def __init__(self,x,y,z=None):
        if z is not None:
            super().__init__("Point",[x,y,z])
        else:
            super().__init__("Point",[x,y])


class LineString(Geometry):
    @classmethod
    def from_json(cls,adict):
        return cls(adict['coordinates'])

    def __init__(self,coords):
        super().__init__("LineString",coords)

class Polygon(Geometry):
    @classmethod
    def from_json(cls,adict):
        return cls(adict['coordinates'])

    def __init__(self,coords):
        super().__init__("Polygon",coords)

def from_json(adict):
    if adict["type"] == "FeatureCollection":
        return FeatureCollection.from_json(adict)
    elif adict["type"] == "Feature":
        return Feature.from_json(adict)
    elif adict["type"] == "Point":
        return Point.from_json(adict)
    else:
        print("Unknown type {}".format(adict["type"]))
    # Zjisti, co je to zac
    # Vytvori objektovou hierarchii
    # Vrati korenovy element (Feature / FeatureCollection / Geometry)


p = Point(10,10)
print(json.dumps(p.to_json()))
f = Feature(p,{"test":"value"})
print(json.dumps(f.to_json()))
print(f.geometry.coordinates)

with open("BEZ_ObjektMPP_b.json") as f:
    adict = json.load(f)
print("Adict")
print(adict)
print(from_json(adict).to_json())
