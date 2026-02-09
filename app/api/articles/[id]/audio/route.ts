import { summariseArticle } from '@/lib/summarise';
import articles from '@/data/articles.json';

export async function GET(
    request: Request,
    { params }: { params: Promise<{ id: string }> }
) {
    const { id } = await params;

    // articles is an array of article objects with id and content properties

    const article = articles.find(a => a.id === id);

    // summarise content
    const summary = await summariseArticle(article.content);
    console.log(summary)
    console.log('Fish key exists:', !!process.env.FISH_API_KEY)

    // // Call fish audio api to generate audio from summary
    // const audioResponse = await fetch('https://api.fish.audio/v1/tts', {
    //     method: 'POST',
    //     headers: {
    //         'Authorization': `Bearer ${process.env.FISH_API_KEY}`,
    //         'Content-Type': 'application/json',
    //         'model': 's1'
    //     },
    //     body: JSON.stringify({ text: summary })
    // })

    // if (!audioResponse.ok) {
    //     const errorText = await audioResponse.text();
    //     console.log('Fish Audio API error:', errorText);
    //     return new Response(`Failed to generate audio: ${errorText}`, { status: 500 });
    // }


    // return new Response(audioResponse.body, {
    //     headers: {
    //         'Content-Type': 'audio/mpeg'
    //     }
    // })
    return new Response('Audio generation not implemented yet', { status: 501 });
}