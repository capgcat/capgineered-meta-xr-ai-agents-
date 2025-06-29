import TasksNavigation from './TasksNavigation'

export const metadata = {
  title: 'Mixed Reality Maintenance Dashboard Task Management',
  description: 'Multiple views to help you manage tasks efficiently',
  openGraph: {
    title: 'Mixed Reality Maintenance Dashboard Task Management',
    description: 'Comprehensive task management system for Mixed Reality Maintenance Dashboard Task ManagementMixed Reality Maintenance System for Industrial Operations operations',
  },
  icons: {
    icon: [
      { url: '/favicon.ico', sizes: 'any' },
      { url: '/icon.png', type: 'image/png', sizes: '32x32' },
    ],
    apple: [
      { url: '/apple-icon.png', type: 'image/png', sizes: '180x180' },
    ],
    other: [
      {
        rel: 'mask-icon',
        url: '/safari-pinned-tab.svg',
        color: '#0f172a', // Dark blue matching your theme
      },
    ],
  },
}

export default function TasksLayout({ children }) {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex flex-col gap-6">
        <div>
          <h1 className="text-3xl font-bold text-white mb-2">XRRepairHub Dashboard</h1>
          <p className="text-zinc-400">Multiple views to help you manage tasks efficiently</p>
        </div>

        <TasksNavigation />
        
        {children}
      </div>
    </div>
  )
}
