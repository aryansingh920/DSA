var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Use(async (context, next) =>
{
    Console.WriteLine($"Incoming {context.Request.Method} {context.Request.Path}");

    await next(); // pass control to next middleware / endpoint

    Console.WriteLine($"Response {context.Response.StatusCode}");
});

app.Use(async (context, next) =>
{
    if (!context.Request.Headers.ContainsKey("X-API-KEY"))
    {
        context.Response.StatusCode = 401;
        await context.Response.WriteAsync("Missing API Key");
        return; // STOP pipeline
    }

    await next();
});



app.Run();
