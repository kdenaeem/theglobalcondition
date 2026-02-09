import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY
})

console.log('API Key exists:', !!process.env.ANTHROPIC_API_KEY)

export async function summariseArticle(article: string): Promise<string> {
    const message = await client.messages.create({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 200,
        messages: [
            {
                role: 'user',
                content: `Summarise this news article in 2-3 sentences, suitable for reading aloud as a brief news update:\n\n${article}`
            }
        ]
    })

    const LLMOutput = message.content[0];

    if (LLMOutput.type == 'text') {
        return LLMOutput.text;
    }

    throw new Error('Unexpected content type from Anthropic API');

}