import {collect} from 'content-structure'
import {fileURLToPath} from 'url';
import {dirname,join} from 'path'

const rootdir = dirname(dirname(fileURLToPath(import.meta.url)))

await collect({
    rootdir:rootdir,
    contentdir:join(rootdir,"cache/fetch/home-website/content"),
    content_ext:["md","json","yml","yaml"],
    assets_ext:["svg","webp","png","jpeg","jpg","xlsx","glb"],
    outdir:join(rootdir,"cache/process/structure/home-website"),
    debug:true
})
