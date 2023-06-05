import sys

def GetUserInput():
    print("Insira os valores para x, y e z (separados por espaço):")
    input_str = input()
    values = input_str.split()
    if len(values) != 3:
        print("Erro: Insira exatamente 3 valores!")
        return GetUserInput()
    try:
        x = int(values[0])
        y = int(values[1])
        z = int(values[2])
        return (x, y, z)
    except ValueError:
        print("Erro: Insira apenas valores numéricos!")
        return GetUserInput()

vectPoints = []

for _ in range(3):
    coord = GetUserInput()
    vectPoints.append(coord)

code = '''import bpy

def GenerateMesh(coords):
    r = 1

    # create the Curve Datablock
    #curveData = bpy.data.curves.new('myCurve', type='CURVE')
    curveData = bpy.data.curves.new('myCurve', type='CURVE')
    curveData.dimensions = '3D'
    curveData.resolution_u = 2

    curveData.bevel_depth = r*0.5;

    # map coords to spline
    polyline = curveData.splines.new('NURBS')

    polyline.points.add(len(coords))
    for i, coord in enumerate(coords):
        x,y,z = coord
        polyline.points[i].co = (x, y, z, 1)

    # create Object
    curveOB = bpy.data.objects.new('myCurve', curveData)

    # attach to scene and validate context

    scn = bpy.context.scene
    #scn.objects.link(curveOB)
    bpy.context.collection.objects.link(curveOB)
    #scn.objects.active = curveOB

    #curveOB.select = True

    bpy.ops.export_scene.gltf(filepath="C:/Users/WellitonMartins/Documents/UFSC/Projeto Especializado/Python/Examples/FileGenerateBySCRIPT")
    #bpy.ops.export_scene.b4w_html(filepath="C:/desenv/ProjetoEspecializado/malha.html")

vectPoints = {0}
GenerateMesh(vectPoints)

bpy.ops.wm.quit_blender()
sys.exit()
'''

code = code.format(vectPoints)

with open('codigoblender.txt', 'w') as file:
    file.write(code)

print(vectPoints)
