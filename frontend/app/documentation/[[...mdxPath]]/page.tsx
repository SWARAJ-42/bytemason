import { generateStaticParamsFor, importPage } from 'nextra/pages'
import { useMDXComponents } from '@/mdx-components'
const components = useMDXComponents({})
 
export const generateStaticParams = generateStaticParamsFor('mdxPath')
 
export async function generateMetadata(props: any) {
  const params = await props.params
  const { metadata } = await importPage(params.mdxPath)
  return metadata
}
 
const Wrapper = components.wrapper
 
export default async function Page(props: any) {
  const params = await props.params
  const result = await importPage(params.mdxPath)
  const { default: MDXContent, toc, metadata } = result
  return (
    <Wrapper toc={toc} metadata={metadata}>
      <MDXContent {...props} params={params} />
    </Wrapper>
  )
}