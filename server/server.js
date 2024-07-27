import express from 'express';
import https from 'https'
import { fileURLToPath } from 'url';
import { join, dirname } from 'path';
import { readFileSync, } from 'fs';
import cors from 'cors';
import {apiRouter} from './api_router.js'

import * as dotenv from 'dotenv'
dotenv.config()

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const outdir = process.env.OUT_DIR
const protocol = (process.env.PROTOCOL==null)?"http":process.env.PROTOCOL
const host = (process.env.HOST==null)?"0.0.0.0":process.env.HOST
const port = (process.env.PORT==null)?"6000":process.env.PORT

const app = express()
app.use(cors())
app.use(express.text({ type: 'text/plain' }))
app.use(express.json())

app.use(apiRouter)

if(outdir != null){
    app.use(express.static(outdir))
}

app.use((req, res, next) => {
    res.status(404).send("Sorry can't find that!")
  })

  
if(protocol == "https"){
      const key = readFileSync(join(__dirname, process.env.KEY_FILE),'utf8')
      const cert = readFileSync(join(__dirname, process.env.CERT_FILE),'utf8')
      const httpsServer = https.createServer({key,cert},app)
      httpsServer.listen(port,host,()=>{
        console.log(`listening on ${protocol}://${host}:${port}`)
    });
}else{
    app.listen(port,host,()=>{
        console.log(`listening on ${protocol}://${host}:${port}`)
    });
}
