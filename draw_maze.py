
from matplotlib import pyplot as plt, colors, patches
from util import *

data = maze

# Draw the grid using pyplot
fig, ax = plt.subplots()
colormap = colors.ListedColormap(["white","black","orange","red","green"])
#colormap = 'binary'

data = np.flipud(data)
ax.invert_yaxis()
plt.pcolormesh(data[::-1],cmap=colormap,edgecolors='k', linewidths=0.1)
ax.axis('off')
red_patch = patches.Patch(edgecolor='k',facecolor='red', label='oil',)
blk_patch = patches.Patch(edgecolor='k',facecolor='black', label='wall',)
wht_patch = patches.Patch(edgecolor='k',facecolor='white', label='free space',)
org_patch = patches.Patch(edgecolor='k',facecolor='orange', label='bump',)
grn_patch = patches.Patch(edgecolor='k',facecolor='green', label='end point',)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5)
          ,handles=[red_patch,blk_patch,wht_patch,org_patch,grn_patch]
          ,fancybox=True,shadow=True)

# # Display the plot
# plt.tight_layout()
# plt.show(block=False)
# plt.pause(1)
# print('Press enter to close the plot')
# input()
# plt.close()
