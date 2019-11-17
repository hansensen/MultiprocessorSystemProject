# # %%
# %run -i './1_vanilla.py'

# # %%
# %run -i './2_vanilla_parallel.py'

# # %%
# %run -i './3_strassen.py'

# # %%
import os
os.system('time python ./1_vanilla.py')
os.system('time python ./2_vanilla_parallel.py')
os.system('time python ./3_strassen.py')