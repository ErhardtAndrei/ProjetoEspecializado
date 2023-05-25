import bpy
import mathutils

# Remove todos os objetos da cena, exceto o objeto principal e objetos do tipo "LAMP" ou "CAMERA"
for obj in bpy.context.scene.objects:
    if obj != bpy.context.active_object and obj.type not in ['LAMP', 'CAMERA']:
        bpy.data.objects.remove(obj, do_unlink=True)

# Seleciona o objeto atual
obj = bpy.context.active_object

# Armazena a posição do objeto principal
pos = obj.location

# Define o número de objetos que serão criados em cada direção
num_obj = 20

# Define a distância entre os objetos
distance = 0.5

# Define a matriz de posições
positions = []
for i in range(-num_obj+1, num_obj):
    for j in range(-num_obj+1, num_obj):
        positions.append(mathutils.Vector((pos.x + i * distance, pos.y + j * distance, pos.z)))

# Loop para criar vários objetos
for i in range(len(positions)):
    
    # Cria uma cópia do objeto
    new_obj = obj.copy()
    
    # Adiciona o objeto à cena
    bpy.context.scene.objects.link(new_obj)
    
    # Define a posição do objeto copiado
    new_obj.location = positions[i]

# Exporta o arquivo HTML
bpy.ops.export_scene.b4w_html(filepath="C:/desenv/ProjetoEspecializado/malha.html")
