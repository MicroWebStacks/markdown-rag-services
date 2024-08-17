import { collect } from 'content-structure';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { promises as fs } from 'fs';
import yaml from 'yaml';

const rootdir = dirname(dirname(fileURLToPath(import.meta.url)));
const manifestPath = join(rootdir, 'manifest.yaml');
const manifestContent = await fs.readFile(manifestPath, 'utf8');
const manifest = yaml.parse(manifestContent);


async function processContentDirectories() {
  try {
    for (const entry of manifest.markdown) {
      const contentdir = join(rootdir, entry.path);
      const outdir = join(rootdir, "cache/process/structure", entry.resource);

      await collect({
        rootdir: rootdir,
        contentdir: contentdir,
        content_ext: ["md", "json", "yml", "yaml"],
        assets_ext: ["svg", "webp", "png", "jpeg", "jpg", "xlsx", "glb"],
        outdir: outdir,
        debug: true
      });
    }
  } catch (error) {
    console.error("Error processing content directories:", error);
  }
}

processContentDirectories();
