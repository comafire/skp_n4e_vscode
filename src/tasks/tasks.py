from invoke import Collection
import skp_env, skp_util

ns = Collection()

if skp_env.VSCODE:
    import vscode
    ns.add_collection(Collection.from_module(vscode), 'vscode')
