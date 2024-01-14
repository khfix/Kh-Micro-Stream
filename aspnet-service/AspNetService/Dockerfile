# Use the SDK image to build the application
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build-env

# Copy only the project file and restore as a distinct layer
COPY AspNetService.csproj ./

# Restore NuGet packages
RUN dotnet restore

# Copy the entire solution and build the application
COPY . ./AspNetService

# Publish the application
RUN dotnet publish -c Release -o publish

# Use the runtime image for the final stage
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /publish

# Copy the published output from the build-env stage
COPY --from=build-env /AspNetService/publish ./

EXPOSE 5232

ENTRYPOINT ["dotnet", "AspNetService.dll"]
