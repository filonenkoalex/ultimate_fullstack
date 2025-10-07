var builder = DistributedApplication.CreateBuilder(args);

var cache = builder.AddRedis("cache");

var apiService = builder.AddProject<Projects.UltimateApp_ApiService>("apiservice")
    .WithHttpHealthCheck("/health");

builder.AddProject<Projects.UltimateApp_Web>("webfrontend")
    .WithExternalHttpEndpoints()
    .WithHttpHealthCheck("/health")
    .WithReference(cache)
    .WaitFor(cache)
    .WithReference(apiService)
    .WaitFor(apiService);

builder.AddNpmApp("react", "../UltimateApp.WebApp")
    .WithReference(apiService)
    .WaitFor(apiService)
    .WithHttpEndpoint(env: "VITE_PORT")
    .WithExternalHttpEndpoints()
    .PublishAsDockerFile();

#pragma warning disable ASPIREHOSTINGPYTHON001
builder.AddUvApp("python", "../UltimateApp.Python", "serve")
#pragma warning restore ASPIREHOSTINGPYTHON001
    .WithExternalHttpEndpoints()
    .WithHttpEndpoint(env: "UVICORN_PORT")
    .WithHttpHealthCheck("/v1/health");

builder.Build().Run();
