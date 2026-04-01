# ¡LÉEME PRIMERO – Guía de Instalación Rápida

Architecture Studio OGUC Chile Edition  
(versión 1.0 – Abril 2026)

## Bienvenido/a

Este es el primer Architecture Studio 100 % adaptado a Chile (OGUC, PRC, MINVU, NCh433, DS 50, DS 61, SII, Conservador, etc.).  
Creado por un Arquitecto OGUC con 15+ años de experiencia para que lo uses directamente en tu flujo de trabajo.

## 1. ¿Qué es este repositorio?

Es un paquete completo de agents + skills + rules + hooks que se instala como plugin en aplicaciones de IA.  
Una vez instalado, solo escribes `/studio` y el sistema te responde con inteligencia 100 % chilena (normativa, due diligence, zonificación, sísmica, eficiencia energética, etc.).

## 2. Requisitos mínimos

- Claude Desktop (versión 0.5 o superior) → Recomendado y 100 % probado
- Cuenta de Anthropic activa
- Acceso a GitHub (para instalar desde repositorio)
- (Opcional) Cursor, Windsurf, Cline o cualquier app que soporte “Claude plugins / custom tools”

## 3. Instalación en CLAUDE DESKTOP (2 minutos)

### Paso a paso:

1. **Crea o clona el repositorio**  
   Ve a GitHub y crea un nuevo repositorio (público o privado).  
   O haz `git clone` desde el link que te entregué anteriormente.

2. Copia TODOS los archivos que te envié en los mensajes anteriores (estructura completa con `.claude-plugin/`, `agents/`, `plugins/`, `rules/`, `hooks/`, etc.).

3. **Abre Claude Desktop**  
   Ve a Customize (arriba a la derecha)

4. Haz clic en **Browse plugins**

5. Haz clic en el botón **+**

6. Selecciona **“Add marketplace from GitHub”**

7. Pega el link completo de tu repositorio  
   Ejemplo: `https://github.com/TU_USUARIO/skills-for-architects-oguc-chile`

8. **Activa el plugin**  
   Claude lo detectará automáticamente como “Architecture Studio – OGUC Chile Edition”.  
   Actívalo (toggle ON).

9. **Prueba inmediata**  
   En cualquier chat nuevo escribe:

```text
/studio Avenida Apoquindo 4500, Las Condes
```

o simplemente:

```text
/studio
```

El dispatcher OGUC Chile tomará el control y te guiará.

## 4. Instalación en otras aplicaciones de IA

| Aplicación | Cómo instalar | Nivel de compatibilidad |
| --- | --- | --- |
| Claude Desktop | Método anterior (recomendado) | ★★★★★ (100 %) |
| Cursor | Copia la carpeta `.claude-plugin` y usa “Custom Tools” o “Claude Projects” | ★★★★☆ (muy buena) |
| Windsurf | Soporta plugins Claude → sigue mismo paso GitHub | ★★★★☆ |
| Cline | Usa “Claude plugin marketplace” | ★★★★☆ |
| VS Code + Continue.dev | Agrega como custom tool (más manual) | ★★★☆☆ |
| ChatGPT / Grok | No compatible (no usan formato `.claude-plugin`) | No recomendado |

Nota importante: El plugin está optimizado para Claude. En otras apps puede funcionar, pero el router y los hooks automáticos funcionan mejor en Claude Desktop.

## 5. Cómo usar (comandos esenciales)

- `/studio` + tu consulta → el router inteligente decide todo
- `/skills` → muestra el menú completo de 42 skills

Ejemplos rápidos:

```text
/studio Due diligence Rol SII 123-45-6789
/studio oguc-coeficientes Avenida Apoquindo 4500
/studio Programa para oficina de 120 personas en Providencia
/studio nch433-analisis 12 pisos, Las Condes
```

## 6. Troubleshooting rápido

| Problema | Solución |
| --- | --- |
| Plugin no aparece | Verifica que la carpeta `.claude-plugin/manifest.json` exista y esté en la raíz |
| Error de hooks | Asegúrate que los archivos `.sh` tengan permisos de ejecución (`chmod +x`) |
| No reconoce direcciones chilenas | Escribe la dirección completa + comuna |
| Disclaimer no aparece | Revisa que la rule `professional-disclaimer-chile.md` esté cargada |

## 7. Disclaimer Legal (obligatorio)

Este plugin es una herramienta de apoyo.  
Nunca sustituye la revisión, firma ni responsabilidad de un arquitecto titulado.  
Toda aprobación final corresponde exclusivamente a la Dirección de Obras Municipales (DOM).

## ¡Listo!

Ya tienes el mejor asistente de arquitectura para Chile instalado.  
Ahora solo abre Claude Desktop y escribe:

```text
/studio
```

¡Bienvenido al futuro del estudio de arquitectura chileno! 🇨🇱
