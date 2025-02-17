from pydantic import BaseModel, Field

class Intent(BaseModel):
    features: list[str] = Field(..., description="Core features extracted from user's request")

class SupabaseTable(BaseModel):
    name: str = Field(..., description="Name of the table")
    schema: str = Field(..., description="SQL schema for creating the table including types and relationships")

class APIRoute(BaseModel):
    path: str = Field(..., description="API route path (e.g., /api/users)")
    method: str = Field(..., description="HTTP method (GET, POST, PUT, DELETE)")
    description: str = Field(..., description="What this API route does and returns")
    query: str = Field(..., description="Supabase query or SQL to be used")

class Page(BaseModel):
    path: str = Field(..., description="Route path (e.g., /dashboard)")
    description: str = Field(..., description="What this page does")
    api_routes: list[str] = Field(..., description="API routes this page uses")
    components: list[str] = Field(..., description="UI components used on this page")

class Component(BaseModel):
    name: str = Field(..., description="Name of the component")
    description: str = Field(..., description="What this component does")
    is_client: bool = Field(..., description="Whether this is a client component")

class ProjectStructure(BaseModel):
    pages: list[Page] = Field(..., description="App pages/routes")
    components: list[Component] = Field(..., description="Reusable UI components")
    api_routes: list[APIRoute] = Field(..., description="API endpoints")
    database: list[SupabaseTable] = Field(..., description="Database tables")


class ProjectSpec(BaseModel):
    name: str = Field(..., description="Project name")
    description: str = Field(..., description="Project purpose")
    features: list[str] = Field(..., description="Features to implement")
    structure: ProjectStructure = Field(..., description="Project structure")